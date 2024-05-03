---
title: keystores
hide_title: false
hide_table_of_contents: false
keywords:
  - keystores
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keystores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.keystores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Resource ID for this keystore. Values must match the regular expression `[\w[:space:].-]&#123;1,255&#125;`. |
| <CopyableCode code="aliases" /> | `array` | Output only. Aliases in this keystore. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_keystores_get" /> | `SELECT` | <CopyableCode code="environmentsId, keystoresId, organizationsId" /> | Gets a keystore or truststore. |
| <CopyableCode code="organizations_environments_keystores_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a keystore or truststore. - Keystore: Contains certificates and their associated keys. - Truststore: Contains trusted certificates used to validate a server's certificate. These certificates are typically self-signed certificates or certificates that are not signed by a trusted CA. |
| <CopyableCode code="organizations_environments_keystores_delete" /> | `DELETE` | <CopyableCode code="environmentsId, keystoresId, organizationsId" /> | Deletes a keystore or truststore. |
