from qgis.PyQt.QtWidgets import QMessageBox,QTextEdit,QSizePolicy,QDialog,QTableView,QAbstractItemView
from qgis.PyQt.QtCore import Qt,QSettings,QEvent

# QT6
try :
    Dialog = Qt.WindowType.Dialog
    Window = Qt.WindowType.Window
    ToolTip = Qt.WindowType.ToolTip
    Rejected = QDialog.DialogCode.Rejected
    WindowCloseButtonHint = Qt.WindowType.WindowCloseButtonHint
    WindowTitleHint = Qt.WindowType.WindowTitleHint
    WindowStaysOnTopHint = Qt.WindowType.WindowStaysOnTopHint
    FramelessWindowHint = Qt.WindowType.FramelessWindowHint
    KeepAspectRatio = Qt.AspectRatioMode.KeepAspectRatio
    SmoothTransformation = Qt.TransformationMode.SmoothTransformation
    Checked = Qt.CheckState.Checked
    Unchecked = Qt.CheckState.Unchecked
    ItemIsEditable = Qt.ItemFlag.ItemIsEditable
    ItemIsEnabled = Qt.ItemFlag.ItemIsEnabled
    ItemIsSelectable = Qt.ItemFlag.ItemIsSelectable
    # ItemIsEnabled = Qt.ItemFlag.ItemIsEnabled
    # ItemIsUserCheckable = Qt.ItemFlag.ItemIsUserCheckable
    # MatchExactly = Qt.MatchFlag.MatchExactly
    # RightSide = QTabBar.ButtonPosition.RightSide
    # LeftSide = QTabBar.ButtonPosition.LeftSide
    Warning = QMessageBox.Icon.Warning
    YesRole = QMessageBox.ButtonRole.YesRole
    AcceptRole = QMessageBox.ButtonRole.AcceptRole
    Ok = QMessageBox.StandardButton.Ok
    # NoSelection = QAbstractItemView.SelectionMode.NoSelection
    # NoFocus = Qt.FocusPolicy.NoFocus
    # DisplayRole = Qt.ItemDataRole.DisplayRole
    # BackgroundRole = Qt.ItemDataRole.BackgroundRole
    RightButton = Qt.MouseButton.RightButton
    MiddleButton = Qt.MouseButton.MiddleButton
    LeftButton = Qt.MouseButton.LeftButton
    # NoContextMenu = Qt.ContextMenuPolicy.NoContextMenu
    AlignCenter = Qt.AlignmentFlag.AlignCenter
    WaitCursor = Qt.CursorShape.WaitCursor
    # AscendingOrder = QtCore.Qt.SortOrder.AscendingOrder
    NoWrap = QTextEdit.LineWrapMode.NoWrap
    ScrollBarAlwaysOff = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    Expanding = QSizePolicy.Policy.Expanding
    CrossCursor = Qt.CursorShape.CrossCursor
    ArrowCursor = Qt.CursorShape.ArrowCursor
    red = Qt.GlobalColor.red
    Horizontal = Qt.Orientation.Horizontal
    NativeFormat = QSettings.Format.NativeFormat
    UserScope = QSettings.Scope.UserScope
    WA_TransparentForMouseEvents = Qt.WidgetAttribute.WA_TransparentForMouseEvents
    SelectRows = QTableView.SelectionBehavior.SelectRows
    SingleSelection = QTableView.SelectionMode.SingleSelection
    NoEditTriggers = QAbstractItemView.EditTrigger.NoEditTriggers
    MouseButtonPress = QEvent.Type.MouseButtonPress
    MouseMove = QEvent.Type.MouseMove
    MouseButtonRelease = QEvent.Type.MouseButtonRelease
    Orientations = Qt.Orientation




# QT5
except AttributeError :
    Dialog = Qt.Dialog
    Window = Qt.Window
    ToolTip = Qt.ToolTip
    Rejected = QDialog.Rejected
    WindowCloseButtonHint = Qt.WindowCloseButtonHint
    WindowTitleHint = Qt.WindowTitleHint
    WindowStaysOnTopHint = Qt.WindowStaysOnTopHint
    FramelessWindowHint = Qt.FramelessWindowHint
    KeepAspectRatio = Qt.KeepAspectRatio
    SmoothTransformation = Qt.SmoothTransformation
    Checked = Qt.Checked
    Unchecked = Qt.Unchecked
    ItemIsEditable = Qt.ItemIsEditable
    ItemIsEnabled = Qt.ItemIsEnabled
    ItemIsSelectable = Qt.ItemIsSelectable
    # ItemIsEnabled = Qt.ItemIsEnabled
    # ItemIsUserCheckable = Qt.ItemIsUserCheckable
    # MatchExactly = Qt.MatchFlag.MatchExactly
    # RightSide = QTabBar.RightSide
    # LeftSide = QTabBar.LeftSide
    Warning = QMessageBox.Warning
    YesRole = QMessageBox.YesRole
    AcceptRole = QMessageBox.AcceptRole
    Ok = QMessageBox.Ok
    # NoSelection = QListWidget.NoSelection
    # NoFocus = Qt.NoFocus
    # DisplayRole = Qt.DisplayRole
    # BackgroundRole = Qt.BackgroundRole
    RightButton = Qt.RightButton
    MiddleButton = Qt.MiddleButton
    LeftButton = Qt.LeftButton
    # NoContextMenu = Qt.NoContextMenu
    AlignCenter = Qt.AlignCenter
    WaitCursor = Qt.WaitCursor
    # AscendingOrder = QtCore.Qt.AscendingOrder
    NoWrap = QTextEdit.NoWrap
    ScrollBarAlwaysOff = Qt.ScrollBarAlwaysOff
    Expanding = QSizePolicy.Expanding
    CrossCursor = Qt.CrossCursor
    ArrowCursor = Qt.ArrowCursor
    red = Qt.red
    Horizontal = Qt.Horizontal
    NativeFormat = QSettings.NativeFormat
    UserScope = QSettings.UserScope
    WA_TransparentForMouseEvents = Qt.WA_TransparentForMouseEvents
    SelectRows = QTableView.SelectRows
    SingleSelection = QTableView.SingleSelection
    NoEditTriggers = QAbstractItemView.NoEditTriggers
    MouseButtonPress = QEvent.MouseButtonPress
    MouseMove = QEvent.MouseMove
    MouseButtonRelease = QEvent.MouseButtonRelease
    Orientations = Qt.Orientations
