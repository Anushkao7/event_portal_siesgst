import Carousel from 'react-bootstrap/Carousel';
import './cur.css';
import 'bootstrap/dist/css/bootstrap.min.css';




function Cur() {
  return (
    <div className='curt'>
    <Carousel >
      <Carousel.Item interval={1000} borderR>
      <img src='https://portal.siesgst.ac.in/static/media/TML2023%20-%204.8b5eb919.jpg' alt='sus'/>
        <Carousel.Caption>
          <h3>First slide label</h3>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item interval={1000}>
        <img src='https://portal.siesgst.ac.in/static/media/TML2023%20-%204.8b5eb919.jpg' alt='sus'/>
        <Carousel.Caption>
          <h3>Second slide label</h3>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
      <img src='https://portal.siesgst.ac.in/static/media/TML2023%20-%204.8b5eb919.jpg' alt='sus'/>
        <Carousel.Caption>
          <h3>Third slide label</h3>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
    </div>
  );
}

export default Cur;