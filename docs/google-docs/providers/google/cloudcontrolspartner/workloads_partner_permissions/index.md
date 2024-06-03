---
title: workloads_partner_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads_partner_permissions
  - cloudcontrolspartner
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
<tr><td><b>Name</b></td><td><code>workloads_partner_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.workloads_partner_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/&#123;organization&#125;/locations/&#123;location&#125;/customers/&#123;customer&#125;/workloads/&#123;workload&#125;/partnerPermissions` |
| <CopyableCode code="partnerPermissions" /> | `array` | The partner permissions granted for the workload |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_partner_permissions" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> |
