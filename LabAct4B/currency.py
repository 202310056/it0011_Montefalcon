exchange_rates = {
    "EUR": 0.931936, "GBP": 0.827816, "JPY": 131.1995, "AUD": 1.439774, "CHF": 0.920289,
    "CAD": 1.342308, "NZD": 1.583391, "TRY": 18.83403, "NGN": 460.3864, "PHP": 54.81473,
    "KGS": 86.20469, "MGA": 4304.102, "SRD": 32.59911, "GHS": 12.17178, "CUP": 1,
    "NOK": 10.29228, "QAR": 3.647457, "CZK": 22.1512, "HRK": 7.362268, "RSD": 108.5081,
    "NIO": 36.54561, "SBD": 8.41428, "MWK": 1026.17, "YER": 250.1646, "VES": 23.11958,
    "BDT": 105.5536, "RON": 4.561703, "DZD": 136.0871, "ARS": 189.5406, "STN": 23.01514,
    "BIF": 2075.047, "MMK": 2099.762, "MUR": 45.34362, "AED": 3.672926, "IDR": 15094.63,
    "MXN": 18.93037, "UAH": 36.47195, "CRC": 582.307, "BZD": 2.015272, "GNF": 8608.203,
    "SZL": 17.51749, "SOS": 568.3301, "INR": 82.61622, "NPR": 132.223, "XAF": 611.4473,
    "AZN": 1.696962, "PYG": 7285.405, "GYD": 210.951, "RWF": 1084.498, "ERN": 15.07319,
    "WST": 2.691706, "BRL": 5.197908, "LKR": 366.2309, "TND": 3.065955, "VND": 23535.79,
    "IQD": 1459.945, "AFN": 90.14747, "NAD": 17.51749, "SYP": 2448.556, "MOP": 8.082523,
    "BAM": 1.823727, "DKK": 6.931757, "PKR": 268.4966, "BGN": 1.821638, "RUB": 73.13025,
    "TMT": 3.499199, "SVC": 8.753525, "XCD": 2.705752, "LAK": 16822.14, "GTQ": 7.840954,
    "SAR": 3.752211, "PLN": 4.412869, "GIP": 0.828083, "GEL": 2.650754, "MKD": 57.30296,
    "AWG": 1.809872, "AOA": 512.4884, "MVR": 15.45372, "BHD": 0.376644, "EGP": 30.36481,
    "KRW": 1260.469, "MRO": 36.02011, "COP": 4746.429, "BBD": 2.018595, "DJF": 177.9833,
    "HNL": 24.64989, "KES": 124.8661, "HKD": 7.848811, "MAD": 10.22721, "ZAR": 17.71922,
    "MDL": 18.7962, "PAB": 1, "FJD": 2.201279, "CDF": 2074.071, "MZN": 64.24781,
    "UGX": 3672.833, "KWD": 0.305558, "THB": 33.40044, "TWD": 30.06651
}

dollar_amount = float(input("How much dollar do you have? "))
currency_code = input("What currency you want to have? ").upper()

if currency_code in exchange_rates:
    converted_amount = dollar_amount * exchange_rates[currency_code]
    print(f"\nDollar: {dollar_amount:.2f} USD")
    print(f"{currency_code}: {converted_amount:.6f}")
else:
    print("Currency code is invalid!")