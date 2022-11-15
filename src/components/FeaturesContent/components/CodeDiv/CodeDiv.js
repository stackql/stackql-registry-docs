import React from 'react';
import clsx from 'clsx';

import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { 
//    twilight, 
//    atomDark,
//    materialDark,
    materialOceanic,
//    nord,
//    okaidia,
//    tomorrow
} from 'react-syntax-highlighter/dist/esm/styles/prism';
//import { 
//    irBlack,
//    obsidian,
//    vs2015,
//    nightOwl,
//    stackoverflowDark
//} from 'react-syntax-highlighter/dist/cjs/styles/hljs';
//import SyntaxHighlighter from 'react-syntax-highlighter';
//import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';

const CodeDiv = props => {
    const {code, isRight} = props;
    return (
        <div 
         //data-aos="fade-right" 
         data-aos={isRight ? "flip-left" : "flip-right"}
         data-aos-easing="ease-out-cubic"
         data-aos-duration="2000"         
         className={clsx('col', 'col--6', 'padding-top--md', 'margin-bottom--md')}
        >
            <SyntaxHighlighter language="sql" style={materialOceanic}>
                {code}
            </SyntaxHighlighter>
        </div>
    );
};

export default CodeDiv;