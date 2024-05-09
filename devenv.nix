{ pkgs, lib, config, inputs, ... }:

{
  packages = [ pkgs.git ];

  scripts.hello.exec = "echo hello from $GREET";

  languages.python.enable = true;
  languages.python.version = "3.12.0";
  languages.python.venv = {
    enable = true;
    requirements = ./requirements.txt;
  };

  scripts.web.exec = ''
    python app
  '';
}
