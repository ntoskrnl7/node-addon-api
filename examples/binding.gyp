{
  "targets": [
    {
      "target_name": "calculator",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
      "include_dirs": [
        "<!@(node -p \"require('..').include\")"
      ],
      "sources": [
        "calculator.h",
        "<!@(node -p \"require('..').generate()\")"
      ]
    }
  ]
}
