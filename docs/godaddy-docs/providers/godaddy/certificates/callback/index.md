---
title: callback
hide_title: false
hide_table_of_contents: false
keywords:
  - callback
  - certificates
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>callback</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.certificates.callback" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="certificate_callback_get" /> | `SELECT` | <CopyableCode code="certificate_id" /> | This method is used to retrieve the registered callback url for a certificate. |
| <CopyableCode code="certificate_callback_delete" /> | `DELETE` | <CopyableCode code="certificate_id" /> | Unregister the callback for a particular certificate. |
| <CopyableCode code="certificate_callback_replace" /> | `EXEC` | <CopyableCode code="callbackUrl, certificate_id" /> | This method is used to register/replace url for callbacks for stateful actions relating to a certificate lifecycle. The callback url is a Webhook style pattern and will receive POST http requests with json body defined in the CertificateAction model definition for each certificate action.  Only one callback URL is allowed to be registered for each certificateId, so it will replace a previous registration. |
