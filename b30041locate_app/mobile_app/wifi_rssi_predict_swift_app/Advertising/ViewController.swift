

import UIKit

final class ViewController: UIViewController {
  @IBOutlet private var tvSlider: UISlider!
  @IBOutlet private var radioSlider: UISlider!
  @IBOutlet private var newspaperSlider: UISlider!
  @IBOutlet private var tvLabel: UILabel!
  @IBOutlet private var radioLabel: UILabel!
  @IBOutlet private var newspaperLabel: UILabel!
  @IBOutlet private var salesLabel: UILabel!
  private let numberFormatter = NumberFormatter()
  private let advertising = Advertising()
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    numberFormatter.numberStyle = .decimal
    numberFormatter.maximumFractionDigits = 1
    
    sliderValueChanged()
  }
  
  @IBAction func sliderValueChanged(_ sender: UISlider? = nil) {
    let hub0 = Double(tvSlider.value)
    let hub1 = Double(radioSlider.value)
    let hub2 = Double(newspaperSlider.value)
    
    let input = AdvertisingInput(hub0: hub0, hub1: hub1, hub2: hub2)

    guard let output = try? advertising.prediction(input: input) else {
      return
    }

    let rssi = output.rssi
    /* according to i2visual_and_analysis.py results */
    var distance = (-rssi + 37)/1.116
    tvLabel.text = numberFormatter.string(from: hub0 as NSNumber)
    radioLabel.text = numberFormatter.string(from: hub1 as NSNumber)
    newspaperLabel.text = numberFormatter.string(from: hub2 as NSNumber)
    
    
    salesLabel.text = numberFormatter.string(from: distance as NSNumber)
  }
}
