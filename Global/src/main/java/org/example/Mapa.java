package org.example;

import java.util.List;

public class Mapa {
    private List<AreaMaterial> areaMaterialList;
    private Localizacao localizacao;

    public Mapa(List<AreaMaterial> areaMaterialList, Localizacao localizacao) {
        this.areaMaterialList = areaMaterialList;
        this.localizacao = localizacao;
    }

    public List<AreaMaterial> getAreaMaterialList() {
        return areaMaterialList;
    }

    public void setAreaMaterialList(List<AreaMaterial> areaMaterialList) {
        this.areaMaterialList = areaMaterialList;
    }

    public Localizacao getLocalizacao() {
        return localizacao;
    }

    public void setLocalizacao(Localizacao localizacao) {
        this.localizacao = localizacao;
    }
}
