@echo off
py -m jschema_to_python ^
    --schema-path sarif-2.1.0-rtm.4.json ^
    --module-name sarif_om ^
    --output-directory sarif_om ^
    --root-class-name SarifLog ^
    --hints-file-path code-gen-hints.json ^
    --force ^
    -vv ^
    %*