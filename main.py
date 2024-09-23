import flet as ft
import api_backend as api

def main(page):

    def get_currency_conversion(e):
        api.key = str(api_key_input_field.value)
        converted_value.value=str(round(float(from_amount_text_box.value) * float(api.get_exchange(str(to_currency_dropdown.value), str(from_currency_dropdown.value))), 2))+" "+str(to_currency_dropdown.value)
        page.update()

    def get_crypto_conversion(e):
        converted_crypto_value.value=str(float(from_amount_text_box.value) * float(api.get_coin_exchange(str(to_currency_dropdown.value), str(from_crypto_dropdown.value))))+" "+str(to_currency_dropdown.value)
        page.update()
    
    def change_page(index):
        if index == 0:
            # Blank "Money" page
            page.controls.clear()
            page.add(
                ft.Column(
                    [
                        ft.Text(value="Money"),
                        converted_value_container,
                        ft.Row(
                            [
                                copy_button,
                            ]
                        ),
                        ft.Divider(height=9, thickness=1),
                        ft.Row(
                            [
                                from_amount_text_box,
                                from_currency_dropdown,
                            ]
                        ),
                        to_currency_dropdown,
                        ft.Row(
                            [
                                submit_button
                            ]
                        )
                    ], 
                alignment=ft.MainAxisAlignment.START, expand=1
                ),
                ft.FloatingActionButton(
                    icon=ft.icons.SETTINGS,
                    on_click=lambda e: change_page(2),
                ),
            )
        elif index == 1:
            # Blank "Crypto" page
            page.controls.clear()
            page.add(
                ft.Column(
                    [
                        ft.Text(value="Crypto"),
                        converted_crypto_value_container,
                        ft.Row(
                            [
                                copy_crypto_button,
                            ]
                        ),
                        ft.Divider(height=9, thickness=1),
                        ft.Row(
                            [
                                from_amount_text_box,
                                from_crypto_dropdown
                            ]
                        ),
                        to_currency_dropdown,                   
                        ft.Row(
                            [
                                submit_button_crypto
                            ]
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START, expand=1),
            )
        elif index == 2:
            page.controls.clear()
            page.add(
                ft.Row(
                    [
                        api_key_input_field
                    ]
                )
            )

        page.update()
    
    def copy_crypto_value(e):
        page.set_clipboard(converted_crypto_value.value)

    def copy_value(e):
        page.set_clipboard(converted_value.value)

    # Update the page when a navbar item is selected
    def on_nav_change(e):
        change_page(e.control.selected_index)

    page.title = "Kantor"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.WALLET, label="Money"),
            ft.NavigationDestination(icon=ft.icons.CURRENCY_BITCOIN, label="Crypto")
        ],
        on_change=on_nav_change
    )

    submit_button = ft.ElevatedButton("Convert", on_click=get_currency_conversion, expand=1, height=40)
    submit_button_crypto = ft.ElevatedButton("Convert", on_click=get_crypto_conversion, expand=1, height=40)

    copy_crypto_button = ft.ElevatedButton("Copy", expand=1, on_click=copy_crypto_value)
    copy_button = ft.ElevatedButton("Copy", expand=1, on_click=copy_value)

    from_amount_text_box = ft.TextField(label="Amount", expand=1)

    api_key_input_field = ft.TextField(label="API key", expand=1)

    converted_value = ft.Text(
        value="", 
        size=30, 
        weight=ft.FontWeight.BOLD,
        color="green",
    )

    converted_crypto_value = ft.Text(
        value="", 
        size=30, 
        weight=ft.FontWeight.BOLD,
        color="green",
    )

    converted_value_container = ft.Container(
        content=converted_value,
        border_radius=ft.border_radius.all(10),
        bgcolor="#14161a",
        padding=15,
        margin=ft.margin.only(),
        alignment=ft.alignment.center,
        border=ft.border.all(1),
    )

    converted_crypto_value_container = ft.Container(
        content=converted_crypto_value,
        border_radius=ft.border_radius.all(10),
        bgcolor="#14161a",
        padding=15,
        margin=ft.margin.only(),
        alignment=ft.alignment.center,
        border=ft.border.all(1),
    )

    from_crypto_dropdown = ft.Dropdown(
        label="Of",
        expand=1,
        options=[
            ft.dropdown.Option("bitcoin"),
            ft.dropdown.Option("ethereum"),
            ft.dropdown.Option("binancecoin"),
            ft.dropdown.Option("ripple"),
            ft.dropdown.Option("cardano"),
            ft.dropdown.Option("dogecoin"),
            ft.dropdown.Option("solana"),
            ft.dropdown.Option("matic-network"),
            ft.dropdown.Option("litecoin"),
            ft.dropdown.Option("polkadot"),
            ft.dropdown.Option("tron"),
            ft.dropdown.Option("avalanche-2"),
            ft.dropdown.Option("uniswap"),
            ft.dropdown.Option("chainlink"),
            ft.dropdown.Option("stellar"),
            ft.dropdown.Option("cosmos"),
            ft.dropdown.Option("ethereum-classic"),
            ft.dropdown.Option("bitcoin-cash"),
            ft.dropdown.Option("near"),
            ft.dropdown.Option("algorand")
        ]
    )

    from_currency_dropdown = ft.Dropdown(
        label="Of",
        expand=1,
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("AED"),
            ft.dropdown.Option("AFN"),
            ft.dropdown.Option("ALL"),
            ft.dropdown.Option("AMD"),
            ft.dropdown.Option("ANG"),
            ft.dropdown.Option("AOA"),
            ft.dropdown.Option("ARS"),
            ft.dropdown.Option("AUD"),
            ft.dropdown.Option("AWG"),
            ft.dropdown.Option("AZN"),
            ft.dropdown.Option("BAM"),
            ft.dropdown.Option("BBD"),
            ft.dropdown.Option("BDT"),
            ft.dropdown.Option("BGN"),
            ft.dropdown.Option("BHD"),
            ft.dropdown.Option("BIF"),
            ft.dropdown.Option("BMD"),
            ft.dropdown.Option("BND"),
            ft.dropdown.Option("BOB"),
            ft.dropdown.Option("BRL"),
            ft.dropdown.Option("BSD"),
            ft.dropdown.Option("BTN"),
            ft.dropdown.Option("BWP"),
            ft.dropdown.Option("BYN"),
            ft.dropdown.Option("BZD"),
            ft.dropdown.Option("CAD"),
            ft.dropdown.Option("CDF"),
            ft.dropdown.Option("CHF"),
            ft.dropdown.Option("CLP"),
            ft.dropdown.Option("CNY"),
            ft.dropdown.Option("COP"),
            ft.dropdown.Option("CRC"),
            ft.dropdown.Option("CUP"),
            ft.dropdown.Option("CVE"),
            ft.dropdown.Option("CZK"),
            ft.dropdown.Option("DJF"),
            ft.dropdown.Option("DKK"),
            ft.dropdown.Option("DOP"),
            ft.dropdown.Option("DZD"),
            ft.dropdown.Option("EGP"),
            ft.dropdown.Option("ERN"),
            ft.dropdown.Option("ETB"),
            ft.dropdown.Option("EUR"),
            ft.dropdown.Option("FJD"),
            ft.dropdown.Option("FKP"),
            ft.dropdown.Option("FOK"),
            ft.dropdown.Option("GBP"),
            ft.dropdown.Option("GEL"),
            ft.dropdown.Option("GGP"),
            ft.dropdown.Option("GHS"),
            ft.dropdown.Option("GIP"),
            ft.dropdown.Option("GMD"),
            ft.dropdown.Option("GNF"),
            ft.dropdown.Option("GTQ"),
            ft.dropdown.Option("GYD"),
            ft.dropdown.Option("HKD"),
            ft.dropdown.Option("HNL"),
            ft.dropdown.Option("HRK"),
            ft.dropdown.Option("HTG"),
            ft.dropdown.Option("HUF"),
            ft.dropdown.Option("IDR"),
            ft.dropdown.Option("ILS"),
            ft.dropdown.Option("IMP"),
            ft.dropdown.Option("INR"),
            ft.dropdown.Option("IQD"),
            ft.dropdown.Option("IRR"),
            ft.dropdown.Option("ISK"),
            ft.dropdown.Option("JEP"),
            ft.dropdown.Option("JMD"),
            ft.dropdown.Option("JOD"),
            ft.dropdown.Option("JPY"),
            ft.dropdown.Option("KES"),
            ft.dropdown.Option("KGS"),
            ft.dropdown.Option("KHR"),
            ft.dropdown.Option("KID"),
            ft.dropdown.Option("KMF"),
            ft.dropdown.Option("KRW"),
            ft.dropdown.Option("KWD"),
            ft.dropdown.Option("KYD"),
            ft.dropdown.Option("KZT"),
            ft.dropdown.Option("LAK"),
            ft.dropdown.Option("LBP"),
            ft.dropdown.Option("LKR"),
            ft.dropdown.Option("LRD"),
            ft.dropdown.Option("LSL"),
            ft.dropdown.Option("LYD"),
            ft.dropdown.Option("MAD"),
            ft.dropdown.Option("MDL"),
            ft.dropdown.Option("MGA"),
            ft.dropdown.Option("MKD"),
            ft.dropdown.Option("MMK"),
            ft.dropdown.Option("MNT"),
            ft.dropdown.Option("MOP"),
            ft.dropdown.Option("MRU"),
            ft.dropdown.Option("MUR"),
            ft.dropdown.Option("MVR"),
            ft.dropdown.Option("MWK"),
            ft.dropdown.Option("MXN"),
            ft.dropdown.Option("MYR"),
            ft.dropdown.Option("MZN"),
            ft.dropdown.Option("NAD"),
            ft.dropdown.Option("NGN"),
            ft.dropdown.Option("NIO"),
            ft.dropdown.Option("NOK"),
            ft.dropdown.Option("NPR"),
            ft.dropdown.Option("NZD"),
            ft.dropdown.Option("OMR"),
            ft.dropdown.Option("PAB"),
            ft.dropdown.Option("PEN"),
            ft.dropdown.Option("PGK"),
            ft.dropdown.Option("PHP"),
            ft.dropdown.Option("PKR"),
            ft.dropdown.Option("PLN"),
            ft.dropdown.Option("PYG"),
            ft.dropdown.Option("QAR"),
            ft.dropdown.Option("RON"),
            ft.dropdown.Option("RSD"),
            ft.dropdown.Option("RUB"),
            ft.dropdown.Option("RWF"),
            ft.dropdown.Option("SAR"),
            ft.dropdown.Option("SBD"),
            ft.dropdown.Option("SCR"),
            ft.dropdown.Option("SDG"),
            ft.dropdown.Option("SEK"),
            ft.dropdown.Option("SGD"),
            ft.dropdown.Option("SHP"),
            ft.dropdown.Option("SLE"),
            ft.dropdown.Option("SLL"),
            ft.dropdown.Option("SOS"),
            ft.dropdown.Option("SRD"),
            ft.dropdown.Option("SSP"),
            ft.dropdown.Option("STN"),
            ft.dropdown.Option("SYP"),
            ft.dropdown.Option("SZL"),
            ft.dropdown.Option("THB"),
            ft.dropdown.Option("TJS"),
            ft.dropdown.Option("TMT"),
            ft.dropdown.Option("TND"),
            ft.dropdown.Option("TOP"),
            ft.dropdown.Option("TRY"),
            ft.dropdown.Option("TTD"),
            ft.dropdown.Option("TVD"),
            ft.dropdown.Option("TWD"),
            ft.dropdown.Option("TZS"),
            ft.dropdown.Option("UAH"),
            ft.dropdown.Option("UGX"),
            ft.dropdown.Option("UYU"),
            ft.dropdown.Option("UZS"),
            ft.dropdown.Option("VES"),
            ft.dropdown.Option("VND"),
            ft.dropdown.Option("VUV"),
            ft.dropdown.Option("WST"),
            ft.dropdown.Option("XAF"),
            ft.dropdown.Option("XCD"),
            ft.dropdown.Option("XDR"),
            ft.dropdown.Option("XOF"),
            ft.dropdown.Option("XPF"),
            ft.dropdown.Option("YER"),
            ft.dropdown.Option("ZAR"),
            ft.dropdown.Option("ZMW"),
            ft.dropdown.Option("ZWL"),
        ],
    )

    to_currency_dropdown = ft.Dropdown(
        label="To",
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("AED"),
            ft.dropdown.Option("AFN"),
            ft.dropdown.Option("ALL"),
            ft.dropdown.Option("AMD"),
            ft.dropdown.Option("ANG"),
            ft.dropdown.Option("AOA"),
            ft.dropdown.Option("ARS"),
            ft.dropdown.Option("AUD"),
            ft.dropdown.Option("AWG"),
            ft.dropdown.Option("AZN"),
            ft.dropdown.Option("BAM"),
            ft.dropdown.Option("BBD"),
            ft.dropdown.Option("BDT"),
            ft.dropdown.Option("BGN"),
            ft.dropdown.Option("BHD"),
            ft.dropdown.Option("BIF"),
            ft.dropdown.Option("BMD"),
            ft.dropdown.Option("BND"),
            ft.dropdown.Option("BOB"),
            ft.dropdown.Option("BRL"),
            ft.dropdown.Option("BSD"),
            ft.dropdown.Option("BTN"),
            ft.dropdown.Option("BWP"),
            ft.dropdown.Option("BYN"),
            ft.dropdown.Option("BZD"),
            ft.dropdown.Option("CAD"),
            ft.dropdown.Option("CDF"),
            ft.dropdown.Option("CHF"),
            ft.dropdown.Option("CLP"),
            ft.dropdown.Option("CNY"),
            ft.dropdown.Option("COP"),
            ft.dropdown.Option("CRC"),
            ft.dropdown.Option("CUP"),
            ft.dropdown.Option("CVE"),
            ft.dropdown.Option("CZK"),
            ft.dropdown.Option("DJF"),
            ft.dropdown.Option("DKK"),
            ft.dropdown.Option("DOP"),
            ft.dropdown.Option("DZD"),
            ft.dropdown.Option("EGP"),
            ft.dropdown.Option("ERN"),
            ft.dropdown.Option("ETB"),
            ft.dropdown.Option("EUR"),
            ft.dropdown.Option("FJD"),
            ft.dropdown.Option("FKP"),
            ft.dropdown.Option("FOK"),
            ft.dropdown.Option("GBP"),
            ft.dropdown.Option("GEL"),
            ft.dropdown.Option("GGP"),
            ft.dropdown.Option("GHS"),
            ft.dropdown.Option("GIP"),
            ft.dropdown.Option("GMD"),
            ft.dropdown.Option("GNF"),
            ft.dropdown.Option("GTQ"),
            ft.dropdown.Option("GYD"),
            ft.dropdown.Option("HKD"),
            ft.dropdown.Option("HNL"),
            ft.dropdown.Option("HRK"),
            ft.dropdown.Option("HTG"),
            ft.dropdown.Option("HUF"),
            ft.dropdown.Option("IDR"),
            ft.dropdown.Option("ILS"),
            ft.dropdown.Option("IMP"),
            ft.dropdown.Option("INR"),
            ft.dropdown.Option("IQD"),
            ft.dropdown.Option("IRR"),
            ft.dropdown.Option("ISK"),
            ft.dropdown.Option("JEP"),
            ft.dropdown.Option("JMD"),
            ft.dropdown.Option("JOD"),
            ft.dropdown.Option("JPY"),
            ft.dropdown.Option("KES"),
            ft.dropdown.Option("KGS"),
            ft.dropdown.Option("KHR"),
            ft.dropdown.Option("KID"),
            ft.dropdown.Option("KMF"),
            ft.dropdown.Option("KRW"),
            ft.dropdown.Option("KWD"),
            ft.dropdown.Option("KYD"),
            ft.dropdown.Option("KZT"),
            ft.dropdown.Option("LAK"),
            ft.dropdown.Option("LBP"),
            ft.dropdown.Option("LKR"),
            ft.dropdown.Option("LRD"),
            ft.dropdown.Option("LSL"),
            ft.dropdown.Option("LYD"),
            ft.dropdown.Option("MAD"),
            ft.dropdown.Option("MDL"),
            ft.dropdown.Option("MGA"),
            ft.dropdown.Option("MKD"),
            ft.dropdown.Option("MMK"),
            ft.dropdown.Option("MNT"),
            ft.dropdown.Option("MOP"),
            ft.dropdown.Option("MRU"),
            ft.dropdown.Option("MUR"),
            ft.dropdown.Option("MVR"),
            ft.dropdown.Option("MWK"),
            ft.dropdown.Option("MXN"),
            ft.dropdown.Option("MYR"),
            ft.dropdown.Option("MZN"),
            ft.dropdown.Option("NAD"),
            ft.dropdown.Option("NGN"),
            ft.dropdown.Option("NIO"),
            ft.dropdown.Option("NOK"),
            ft.dropdown.Option("NPR"),
            ft.dropdown.Option("NZD"),
            ft.dropdown.Option("OMR"),
            ft.dropdown.Option("PAB"),
            ft.dropdown.Option("PEN"),
            ft.dropdown.Option("PGK"),
            ft.dropdown.Option("PHP"),
            ft.dropdown.Option("PKR"),
            ft.dropdown.Option("PLN"),
            ft.dropdown.Option("PYG"),
            ft.dropdown.Option("QAR"),
            ft.dropdown.Option("RON"),
            ft.dropdown.Option("RSD"),
            ft.dropdown.Option("RUB"),
            ft.dropdown.Option("RWF"),
            ft.dropdown.Option("SAR"),
            ft.dropdown.Option("SBD"),
            ft.dropdown.Option("SCR"),
            ft.dropdown.Option("SDG"),
            ft.dropdown.Option("SEK"),
            ft.dropdown.Option("SGD"),
            ft.dropdown.Option("SHP"),
            ft.dropdown.Option("SLE"),
            ft.dropdown.Option("SLL"),
            ft.dropdown.Option("SOS"),
            ft.dropdown.Option("SRD"),
            ft.dropdown.Option("SSP"),
            ft.dropdown.Option("STN"),
            ft.dropdown.Option("SYP"),
            ft.dropdown.Option("SZL"),
            ft.dropdown.Option("THB"),
            ft.dropdown.Option("TJS"),
            ft.dropdown.Option("TMT"),
            ft.dropdown.Option("TND"),
            ft.dropdown.Option("TOP"),
            ft.dropdown.Option("TRY"),
            ft.dropdown.Option("TTD"),
            ft.dropdown.Option("TVD"),
            ft.dropdown.Option("TWD"),
            ft.dropdown.Option("TZS"),
            ft.dropdown.Option("UAH"),
            ft.dropdown.Option("UGX"),
            ft.dropdown.Option("UYU"),
            ft.dropdown.Option("UZS"),
            ft.dropdown.Option("VES"),
            ft.dropdown.Option("VND"),
            ft.dropdown.Option("VUV"),
            ft.dropdown.Option("WST"),
            ft.dropdown.Option("XAF"),
            ft.dropdown.Option("XCD"),
            ft.dropdown.Option("XDR"),
            ft.dropdown.Option("XOF"),
            ft.dropdown.Option("XPF"),
            ft.dropdown.Option("YER"),
            ft.dropdown.Option("ZAR"),
            ft.dropdown.Option("ZMW"),
            ft.dropdown.Option("ZWL"),
        ],
    )

    change_page(0)

ft.app(main)