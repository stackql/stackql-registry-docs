---
title: service_replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - service_replicas
  - service_fabric_mesh
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

Creates, updates, deletes, gets or lists a <code>service_replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.service_replicas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="codePackages" /> | `array` | Describes the set of code packages that forms the service. A code package describes the container and the properties for running it. All the code packages are started together on the same host and share the same context (network, process etc.). |
| <CopyableCode code="diagnostics" /> | `object` | Reference to sinks in DiagnosticsDescription. |
| <CopyableCode code="networkRefs" /> | `array` | The names of the private networks that this service needs to be part of. |
| <CopyableCode code="osType" /> | `string` | The operation system required by the code in service. |
| <CopyableCode code="replicaName" /> | `string` | Name of the replica. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationResourceName, replicaName, resourceGroupName, serviceResourceName, subscriptionId" /> | Gets the information about the service replica with the given name. The information include the description and other properties of the service replica. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationResourceName, resourceGroupName, serviceResourceName, subscriptionId" /> | Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance. |

## `SELECT` examples

Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.


```sql
SELECT
codePackages,
diagnostics,
networkRefs,
osType,
replicaName
FROM azure.service_fabric_mesh.service_replicas
WHERE applicationResourceName = '{{ applicationResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceResourceName = '{{ serviceResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```