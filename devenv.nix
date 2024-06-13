{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    version = "3.12.0";
    venv = {
      enable = true;
      requirements = ./requirements.txt;
    };
  };

  processes.web.exec = "python app";
}
