---
title: dns_record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_record_sets
  - servicenetworking
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
<tr><td><b>Name</b></td><td><code>dns_record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.dns_record_sets" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="servicesId" /> | Producers can use this method to retrieve a list of available DNS RecordSets available inside the private zone on the tenant host project accessible from their network. |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="servicesId" /> | Service producers can use this method to add DNS record sets to private DNS zones in the shared producer host project. |
| <CopyableCode code="remove" /> | `EXEC` | <CopyableCode code="servicesId" /> | Service producers can use this method to remove DNS record sets from private DNS zones in the shared producer host project. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="servicesId" /> | Service producers can use this method to update DNS record sets from private DNS zones in the shared producer host project. |
