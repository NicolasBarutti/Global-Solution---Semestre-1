package org.example;

public class Material {
    private TipoMaterial tipoMaterial;
    private AreaMaterial areaMaterial;

    public Material(TipoMaterial tipoMaterial, AreaMaterial areaMaterial) {
        this.tipoMaterial = tipoMaterial;
        this.areaMaterial = areaMaterial;
    }

    public TipoMaterial getTipoMaterial() {
        return tipoMaterial;
    }

    public void setTipoMaterial(TipoMaterial tipoMaterial) {
        this.tipoMaterial = tipoMaterial;
    }

    public AreaMaterial getAreaMaterial() {
        return areaMaterial;
    }

    public void setAreaMaterial(AreaMaterial areaMaterial) {
        this.areaMaterial = areaMaterial;
    }
}
