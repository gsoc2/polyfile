from abnf.grammars.misc import load_grammar_rules
from abnf.grammars import rfc9110, rfc3986
from abnf import Rule as _Rule
from typing import List, Tuple


class Rule(_Rule):
    """Request headers defined as 'experimental' by the Mozilla developer documentation, which have partial cross browser support.

    Many of these headers convey client hints (indicated by the CH segment in some, but not all, related header names).

    Most of these also require only simple ABNF to string together the values, so they are collected here for brevity.
    """

    grammar: List[str] = [
        'experimental-header = "Device-Memory:" OWS Device-Memory OWS / "Downlink:" OWS Downlink OWS / "Early-Data:" OWS Early-Data OWS / "ECT:" OWS ECT OWS / "RTT:" OWS RTT OWS / "Save-Data:" OWS Save-Data OWS / "Sec-CH-UA-Arch:" OWS Sec-CH-UA-Arch OWS / "Sec-CH-UA-Bitness:" OWS Sec-CH-UA-Bitness OWS / "Sec-CH-UA-Full-Version-List:" OWS Sec-CH-UA-Full-Version-List OWS / "Sec-CH-UA-Mobile:" OWS Sec-CH-UA-Mobile OWS / "Sec-CH-UA-Model:" OWS Sec-CH-UA-Model OWS / "Sec-CH-UA-Platform:" OWS Sec-CH-UA-Platform OWS / "Sec-CH-UA-Platform-Version:" OWS Sec-CH-UA-Platform-Version OWS / "Sec-GPC:" OWS Sec-GPC OWS / "Sec-CH-Prefers-Reduced-Motion:" OWS Sec-CH-Prefers-Reduced-Motion OWS / "Sec-WebSocket-Accept:" OWS Sec-WebSocket-Accept OWS',
        # https://www.w3.org/TR/device-memory/#iana-device-memory
        'Device-Memory = "0.25" / "0.5" / "1" / "2" / "4" / "8',
        # https://datatracker.ietf.org/doc/html/rfc8941#section-3.3.2
        'sf-decimal  = ["-"] 1*12DIGIT "." 1*3DIGIT',
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Downlink
        # https://wicg.github.io/netinfo/#dom-networkinformation-downlink
        "Downlink = sf-decimal",
        # https://httpwg.org/specs/rfc8470.html#header
        'Early-Data = "1"',
        # https://wicg.github.io/netinfo/#ect-request-header-field
        'ECT = "2g" / "3g" / "4g" / "slow-2g"',
        # https://wicg.github.io/netinfo/#rtt-request-header-field
        "RTT = TODO",
        # https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-header-structure-15
        # https://wicg.github.io/savedata/#save-data-request-header-field follows the Structured Headers RFC for sh-list (TODO kaoudis: move structured headers abnf to its own file)
        'Save-Data = "on" / sh-list',
        'sh-list = list-member *( *SP "," *SP list-member )',
        "list-member = sh-item / inner-list",
        'inner-list    = "(" *SP [ sh-item *( 1*SP sh-item ) *SP ] ")" *parameter',
        "sh-item   = bare-item *parameter",
        "bare-item = sh-integer / sh-decimal / sh-string / sh-token / sh-binary / sh-boolean",
        'sh-integer = ["-"] 1*15DIGIT',
        'sh-decimal  = ["-"] 1*12DIGIT "." 1*3DIGIT',
        "sh-string = DQUOTE *(chr) DQUOTE",
        "chr       = unescaped / escaped",
        "unescaped = %x20-21 / %x23-5B / %x5D-7E",
        'escaped   = "" ( DQUOTE / "" )',
        'sh-token = ( ALPHA / "\*" ) *( tchar / ":" / "/" )',
        'sh-binary = ":" *(base64) ":"',
        'base64    = ALPHA / DIGIT / "+" / "/" / "="',
        'sh-boolean = "?" boolean',
        'boolean    = "0" / "1"',
        # https://wicg.github.io/user-preference-media-features-headers/#sec-ch-prefers-reduced-motion
        "Sec-CH-Prefers-Reduced-Motion = TODO",
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-CH-UA
        "Sec-CH-UA = TODO",
        # https://wicg.github.io/ua-client-hints/#sec-ch-ua-arch
        "Sec-CH-UA-Arch = TODO",
        # https://wicg.github.io/ua-client-hints/#sec-ch-ua-bitness
        "Sec-CH-UA-Bitness = TODO",
        # https://wicg.github.io/ua-client-hints/#sec-ch-ua-full-version
        "Sec-CH-UA-Full-Version = TODO",
        # https://wicg.github.io/ua-client-hints/#sec-ch-ua-full-version-list
        "Sec-CH-UA-Full-Version-List = TODO",
        # https://wicg.github.io/ua-client-hints/#sec-ch-ua-mobile
        "Sec-CH-UA-Mobile = TODO",
        # https://wicg.github.io/ua-client-hints/#sec-ch-ua-model
        "Sec-CH-UA-Model = TODO",
        # https://wicg.github.io/ua-client-hints/#sec-ch-ua-platform
        "Sec-CH-UA-Platform = TODO",
        # https://wicg.github.io/ua-client-hints/#sec-ch-ua-platform-version
        "Sec-CH-UA-Platform-Version = TODO",
        # https://privacycg.github.io/gpc-spec/#the-sec-gpc-header-field-for-http-requests
        "Sec-GPC = TODO",
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-WebSocket-Accept
        "Sec-WebSocket-Accept = TODO",
    ]
