import React from 'react';
import Terminal from '../../modules/react-animated-term/lib'
import '../../modules/react-animated-term/dist/react-animated-term.css'

const Code = props => {
    const { data } = props;
    return (
        <Terminal
        lines={data.termLines}
        interval={5}
        white
      />

    );
};
        
export default Code;