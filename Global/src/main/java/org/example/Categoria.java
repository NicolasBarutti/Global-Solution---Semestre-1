package org.example;

public class Categoria {
    private Material material;
    private NaoColetaveis naoColetaveis;

    public Categoria(Material material, NaoColetaveis naoColetaveis) {
        this.material = material;
        this.naoColetaveis = naoColetaveis;
    }

    public Material getMaterial() {
        return material;
    }

    public void setMaterial(Material material) {
        this.material = material;
    }

    public NaoColetaveis getNaoColetaveis() {
        return naoColetaveis;
    }

    public void setNaoColetaveis(NaoColetaveis naoColetaveis) {
        this.naoColetaveis = naoColetaveis;
    }

    public void getPriovidadeColeta(){

    }
}
