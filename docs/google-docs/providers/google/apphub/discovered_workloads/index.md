
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>discovered_workload</code> resource or lists <code>discovered_workloads</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discovered_workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apphub.discovered_workloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the discovered workload. Format: "projects/{host-project-id}/locations/{location}/discoveredWorkloads/{uuid}" |
| <CopyableCode code="workloadProperties" /> | `object` | Properties of an underlying compute resource represented by the Workload. |
| <CopyableCode code="workloadReference" /> | `object` | Reference of an underlying compute resource represented by the Workload. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="discoveredWorkloadsId, locationsId, projectsId" /> | Gets a Discovered Workload in a host project and location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Discovered Workloads that can be added to an Application in a host project and location. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists a Discovered Workload in a host project and location, with a given resource URI. |

## `SELECT` examples

Lists Discovered Workloads that can be added to an Application in a host project and location.

```sql
SELECT
name,
workloadProperties,
workloadReference
FROM google.apphub.discovered_workloads
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
