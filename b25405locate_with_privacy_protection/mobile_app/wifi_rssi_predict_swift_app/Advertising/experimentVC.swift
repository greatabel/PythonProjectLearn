import UIKit

// 对于高度等参数采用宏定义
fileprivate let cRecordH: CGFloat = 40

class experimentVC: UIViewController {
    
    // 控件
    @IBOutlet weak var showLabel: UILabel!
//    @IBOutlet weak var rightButton: UIButton!
//
//    @IBOutlet weak var leftButton: UIButton!
    
    var timer: Timer!
    
    // 数据变量
    var isStart: Bool = false
    var recordCnt: Int = 0
    var msCnt: Int = 0
    var cMaxLabelNum: Int!
    var cButtonH: CGFloat!
    var recordArray: [UILabel]!
    
  
    override func viewDidLoad() {
        
        setupUI()
      print("begin test rssi")
        var rssi_strength = mock_wifiStrength()
        print(rssi_strength)
        let numberFormatter = NumberFormatter()
        if rssi_strength != nil {
            print("rssi_strength contains some integer value.")
          showLabel.text = numberFormatter.string(from: rssi_strength! as NSNumber)
        } else {
          showLabel.text = "0"
        }
        
    }
    
 
    
    
    
}

extension experimentVC {
    
    func setupUI() {
        
        // 由于采用深色背景，状态栏设置浅色
        UIApplication.shared.statusBarStyle = .lightContent
        

    }
    

    
}

private func wifiStrength() -> Int? {
    let app = UIApplication.shared
    var rssi: Int?
    guard let statusBar = app.value(forKey: "statusBar") as? UIView, let foregroundView = statusBar.value(forKey: "foregroundView") as? UIView else {
        return rssi
    }
    for view in foregroundView.subviews {
        if let statusBarDataNetworkItemView = NSClassFromString("UIStatusBarDataNetworkItemView"), view .isKind(of: statusBarDataNetworkItemView) {
            if let val = view.value(forKey: "wifiStrengthRaw") as? Int {
                //print("rssi: \(val)")

                rssi = val
                break
            }
        }
    }
    return rssi
}

private func mock_wifiStrength() -> Int? {
    let app = UIApplication.shared
    var rssi: Int?
    rssi = Int(arc4random_uniform(200) + 1)

    return rssi
}
