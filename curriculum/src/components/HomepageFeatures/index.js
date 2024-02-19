import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'BTG - Estágio de Férias',
    Image: require('@site/static/img/btg_fernando.jpeg').default,
    description: (
      <>
        Durante o estágio, fui responsável por desenvolver o front-end em <code>react</code>, utilizando do design system da empressa. Além disso, participei na prototipação do figma e criação de componentes.
      </>
    ),
  },{
    title: 'Iniciação Científica - PIBIC-EM',
    Image: require('@site/static/img/safetytracker.png').default,
    description: (
      <>
        Desenvolvi, com uma equipe de 4 pessoas, uma aplicação web para a previsão de acidentes em rodovias federais, com o uso de Machine Learning.
      </>
    ),
  },
  {
    title: 'Módulo 1 - Gameficação',
    href:"https://github.com/2023M1T9-Inteli/grupo2",
    Image: require('@site/static/img/grupo-cia-de-talentos.png').default,
    description: (
      <>
        Jogo desenvolvido em <code>GDScript</code> para a Cia de Talentos, no qual o objetivo final era o ensinamento de gestão de tempo.
      </>
    ),
  },
  {
    title: 'Módulo 2 - Página Web',
    Image: require('@site/static/img/panpedia.jpg').default,
    description: (
      <>
        Aplicação Web feita com <code>EJS, Javascript e HTML</code> para a centralização do metadados do banco de dados do Banco Pan.
      </>
    ),
  },
  {
    title: 'Módulo 3 - Machine Learning',
    Image: require('@site/static/img/mobly.png').default,
    description: (
      <>
        Criação de um modelo de Machine Learning para a predição de venda de móveis conforme a época do ano.  
      </>
    ),
  },
  {
    title: 'Módulo 4 - IOT',
    Image: require('@site/static/img/ipt.png').default,
    description: (
      <>
        Projeto em parceira com o IPT para a criação de uma célula de carga, capaz de detectar variações em estruturas civis. A célula foi feita utilizando esp32.
      </>
    ),
  },
];

function Feature({title, description,href,Image}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <img className={styles.featureSvg} src={Image} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <a href={href}><Heading as="h3">{title}</Heading></a>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
