---
title: developers_monetization_config
hide_title: false
hide_table_of_contents: false
keywords:
  - developers_monetization_config
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
<tr><td><b>Name</b></td><td><code>developers_monetization_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.developers_monetization_config" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_developers_get_monetization_config" /> | `SELECT` | <CopyableCode code="developersId, organizationsId" /> | Gets the monetization configuration for the developer. |
| <CopyableCode code="organizations_developers_update_monetization_config" /> | `EXEC` | <CopyableCode code="developersId, organizationsId" /> | Updates the monetization configuration for the developer. |
