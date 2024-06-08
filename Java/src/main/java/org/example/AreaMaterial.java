package org.example;

public class AreaMaterial {
    private Double altura, largura; // Tamanhos no eixo X e eixo Y

    public AreaMaterial(Double altura, Double largura) {
        this.altura = altura;
        this.largura = largura;
    }

    public Double getAltura() {
        return altura;
    }

    public void setAltura(Double altura) {
        this.altura = altura;
    }

    public Double getLargura() {
        return largura;
    }

    public void setLargura(Double largura) {
        this.largura = largura;
    }


    //metodo para calcular a area do material escaniado (é clalculado o produto dos atributos da classe)
    public double getAreaMaterial(){
        return altura * largura;
    }
}
