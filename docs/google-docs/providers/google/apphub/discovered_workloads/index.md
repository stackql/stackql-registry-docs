---
title: discovered_workloads
hide_title: false
hide_table_of_contents: false
keywords:
  - discovered_workloads
  - apphub
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
<tr><td><b>Name</b></td><td><code>discovered_workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apphub.discovered_workloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the discovered workload. Format: "projects/&#123;host-project-id&#125;/locations/&#123;location&#125;/discoveredWorkloads/&#123;uuid&#125;" |
| <CopyableCode code="workloadProperties" /> | `object` | Properties of an underlying compute resource represented by the Workload. |
| <CopyableCode code="workloadReference" /> | `object` | Reference of an underlying compute resource represented by the Workload. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="discoveredWorkloadsId, locationsId, projectsId" /> | Gets a Discovered Workload in a host project and location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Discovered Workloads that can be added to an Application in a host project and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Discovered Workloads that can be added to an Application in a host project and location. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists a Discovered Workload in a host project and location, with a given resource URI. |
