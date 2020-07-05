/*
Navicat MySQL Data Transfer

Source Server         : cudeg
Source Server Version : 50562
Source Host           : us-cdbr-east-02.cleardb.com:3306
Source Database       : heroku_2bef9f5656163b1

Target Server Type    : MYSQL
Target Server Version : 50562
File Encoding         : 65001

Date: 2020-07-05 20:20:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bdambevlearning
-- ----------------------------
DROP TABLE IF EXISTS `bdambevlearning`;
CREATE TABLE `bdambevlearning` (
  `idPost` int(11) DEFAULT NULL,
  `strTitulo` varchar(255) DEFAULT NULL,
  `strDescricao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdassinaturas
-- ----------------------------
DROP TABLE IF EXISTS `bdassinaturas`;
CREATE TABLE `bdassinaturas` (
  `idAssinatura` int(11) NOT NULL AUTO_INCREMENT,
  `idProduto` int(11) DEFAULT NULL,
  `idCliente` int(11) DEFAULT NULL,
  `tmTempo` datetime DEFAULT NULL,
  PRIMARY KEY (`idAssinatura`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdbar
-- ----------------------------
DROP TABLE IF EXISTS `bdbar`;
CREATE TABLE `bdbar` (
  `idBar` int(11) NOT NULL AUTO_INCREMENT,
  `strNome` varchar(100) DEFAULT NULL,
  `strEmail` varchar(150) DEFAULT NULL,
  `strSenha` varchar(255) DEFAULT NULL,
  `strEndereco` varchar(150) DEFAULT NULL,
  `intCNPJ` int(20) DEFAULT NULL,
  `strLogo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idBar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdcerveja
-- ----------------------------
DROP TABLE IF EXISTS `bdcerveja`;
CREATE TABLE `bdcerveja` (
  `idCerveja` int(11) NOT NULL AUTO_INCREMENT,
  `idMarca` int(11) DEFAULT NULL,
  `strTitulo` varchar(255) DEFAULT NULL,
  `dblTeor` double(10,0) DEFAULT NULL,
  `strDescricao` varchar(255) DEFAULT NULL,
  `strTipo` varchar(100) DEFAULT NULL,
  `strFamilia` varchar(255) DEFAULT NULL,
  `strCor` varchar(50) DEFAULT NULL,
  `strTemp` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idCerveja`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdcliente
-- ----------------------------
DROP TABLE IF EXISTS `bdcliente`;
CREATE TABLE `bdcliente` (
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `strNome` varchar(200) DEFAULT NULL,
  `strFotodePerfil` varchar(200) DEFAULT NULL,
  `intPersona` int(11) DEFAULT NULL,
  `strEmail` varchar(255) DEFAULT NULL,
  `strSenha` varchar(255) DEFAULT NULL,
  `strEndereco` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdconquista
-- ----------------------------
DROP TABLE IF EXISTS `bdconquista`;
CREATE TABLE `bdconquista` (
  `idConquista` int(11) NOT NULL AUTO_INCREMENT,
  `idInsignea` int(11) DEFAULT NULL,
  `idCliente` int(11) DEFAULT NULL,
  PRIMARY KEY (`idConquista`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bdevento
-- ----------------------------
DROP TABLE IF EXISTS `bdevento`;
CREATE TABLE `bdevento` (
  `idEvento` int(11) NOT NULL AUTO_INCREMENT,
  `idBar` int(11) DEFAULT NULL,
  `strTitulo` varchar(255) DEFAULT NULL,
  `srtDescricao` varchar(255) DEFAULT NULL,
  `strFoto` varchar(255) DEFAULT NULL,
  `dtData` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idEvento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdfavoritocol
-- ----------------------------
DROP TABLE IF EXISTS `bdfavoritocol`;
CREATE TABLE `bdfavoritocol` (
  `idFavoritoCol` int(11) NOT NULL AUTO_INCREMENT,
  `idCliente` int(11) DEFAULT NULL,
  `idCerveja` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idFavoritoCol`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdfavoritos
-- ----------------------------
DROP TABLE IF EXISTS `bdfavoritos`;
CREATE TABLE `bdfavoritos` (
  `idFavoritos` int(11) NOT NULL AUTO_INCREMENT,
  `idCliente` int(11) DEFAULT NULL,
  `idCerveja` int(11) DEFAULT NULL,
  PRIMARY KEY (`idFavoritos`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdinsigena
-- ----------------------------
DROP TABLE IF EXISTS `bdinsigena`;
CREATE TABLE `bdinsigena` (
  `idInsignea` int(11) NOT NULL AUTO_INCREMENT,
  `strNome` varchar(255) DEFAULT NULL,
  `strDescricao` varchar(255) DEFAULT NULL,
  `strFoto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idInsignea`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bdmarcascervejas
-- ----------------------------
DROP TABLE IF EXISTS `bdmarcascervejas`;
CREATE TABLE `bdmarcascervejas` (
  `idMarca` int(11) NOT NULL AUTO_INCREMENT,
  `strTitulo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idMarca`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdpedido
-- ----------------------------
DROP TABLE IF EXISTS `bdpedido`;
CREATE TABLE `bdpedido` (
  `idPedido` int(11) NOT NULL AUTO_INCREMENT,
  `idBar` int(11) DEFAULT NULL,
  `idProduto` int(11) DEFAULT NULL,
  `idCliente` int(11) DEFAULT NULL,
  `intTipoEntrega` int(11) DEFAULT NULL,
  `intTipoPagamento` int(11) DEFAULT NULL,
  `intStatus` int(11) DEFAULT NULL,
  `intQuantidade` int(11) DEFAULT NULL,
  PRIMARY KEY (`idPedido`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdproduto
-- ----------------------------
DROP TABLE IF EXISTS `bdproduto`;
CREATE TABLE `bdproduto` (
  `idProduto` int(11) NOT NULL AUTO_INCREMENT,
  `idBar` int(11) DEFAULT NULL,
  `strTitulo` varchar(100) DEFAULT NULL,
  `strDescricao` longtext,
  `dblPreco` double(10,0) DEFAULT NULL,
  `intTipo` int(1) DEFAULT NULL,
  `strFoto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idProduto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for bdreview
-- ----------------------------
DROP TABLE IF EXISTS `bdreview`;
CREATE TABLE `bdreview` (
  `idReview` int(11) NOT NULL AUTO_INCREMENT,
  `idBar` int(11) DEFAULT NULL,
  `idCliente` int(11) DEFAULT NULL,
  `strReview` varchar(255) DEFAULT NULL,
  `intEstrelas` int(11) DEFAULT NULL,
  PRIMARY KEY (`idReview`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
