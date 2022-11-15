import React from 'react';
import { useEffect } from "react";

const HubspotContactForm = props => {
    const { region, portalId, formId } = props;
    useEffect(() => {
        const script = document.createElement('script');
        script.src = 'https://js.hsforms.net/forms/shell.js';
        document.body.appendChild(script);
        
        script.addEventListener('load', () => {
            if(window.hbspt) {
              window.hbspt.forms.create({
              region: region,
              portalId: portalId,
              formId: formId,
              target: '#hubspotForm'
            });
          };
        });
      }, []);

      return (
        <div>
            <div id="hubspotForm"></div>
        </div>
    );
}

export default HubspotContactForm;