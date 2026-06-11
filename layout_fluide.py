from PyQt5.QtCore import Qt,QRect, QSize, QPoint
from PyQt5.QtWidgets import QLayout, QSizePolicy, QWidgetItem, QLayoutItem

class LayoutFluide(QLayout):
    def __init__(self, parent=None, margin=0, spacing=0, largeur_max_ligne=1000):
        super().__init__(parent)
        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)
        self.setSpacing(spacing)
        self.itemList = []
        self.largeur_max_ligne = largeur_max_ligne  # limite de largeur avant retour à la ligne

    def index_of_widget(self, widget):
        for i, item in enumerate(self.itemList):
            if item.widget() == widget:
                return i
        return None

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        return self.itemList[index] if 0 <= index < len(self.itemList) else None

    def takeAt(self, index):
        return self.itemList.pop(index) if 0 <= index < len(self.itemList) else None

    def expandingDirections(self):
        # le layout s’étend dans les deux directions
        return Qt.Orientations(Qt.Horizontal)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        """Appelée automatiquement quand le QDialog est redimensionné"""
        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        total_width = 0
        line_height = 0
        max_width = self.largeur_max_ligne
        x = 0

        for item in self.itemList:
            w = item.sizeHint().width()
            h = item.sizeHint().height()
            if x + w > max_width:
                x = 0
                line_height += h + self.spacing()
            x += w + self.spacing()
            total_width = max(total_width, x)

        total_height = line_height + max([item.sizeHint().height() for item in self.itemList])

        margins = self.contentsMargins()
        return QSize(total_width + margins.left() + margins.right(),
                     total_height + margins.top() + margins.bottom())


    def minimumSize(self):
        """Taille minimale calculée d’après les widgets contenus"""
        size = QSize()
        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())
        margins = self.contentsMargins()
        size += QSize(margins.left() + margins.right(), margins.top() + margins.bottom())
        return size

    def doLayout(self, rect, testOnly):
        """Dispose les widgets horizontalement puis passe à la ligne au-delà de largeur_max_ligne"""

        x, y, lineHeight = rect.x(), rect.y(), 0
        # gege
        # max_width = min(rect.width(), self.largeur_max_ligne)
        max_width = rect.width() if rect.width() > 0 else self.largeur_max_ligne

        for item in self.itemList:
            wid = item.widget()
            if not wid:
                continue

            spaceX = self.spacing()
            spaceY = self.spacing()
            nextX = x + item.sizeHint().width() + spaceX

            # Retour à la ligne si on dépasse la largeur max
            if nextX > rect.x() + max_width and lineHeight > 0:
                x = rect.x()
                y += lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()

