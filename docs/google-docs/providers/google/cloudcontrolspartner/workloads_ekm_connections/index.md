---
title: workloads_ekm_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads_ekm_connections
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
<tr><td><b>Name</b></td><td><code>workloads_ekm_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.workloads_ekm_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/&#123;organization&#125;/locations/&#123;location&#125;/customers/&#123;customer&#125;/workloads/&#123;workload&#125;/ekmConnections` |
| <CopyableCode code="ekmConnections" /> | `array` | The EKM connections associated with the workload |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_ekm_connections" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> |
