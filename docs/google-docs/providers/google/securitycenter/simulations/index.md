---
title: simulations
hide_title: false
hide_table_of_contents: false
keywords:
  - simulations
  - securitycenter
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

Creates, updates, deletes, gets or lists a <code>simulations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.simulations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Full resource name of the Simulation: `organizations/123/simulations/456` |
| <CopyableCode code="cloudProvider" /> | `string` | Indicates which cloud provider was used in this simulation. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time simulation was created |
| <CopyableCode code="resourceValueConfigsMetadata" /> | `array` | Resource value configurations' metadata used in this simulation. Maximum of 100. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_simulations_get" /> | `SELECT` | <CopyableCode code="organizationsId, simulationsId" /> | Get the simulation by name or the latest simulation for the given organization. |

## `SELECT` examples

Get the simulation by name or the latest simulation for the given organization.

```sql
SELECT
name,
cloudProvider,
createTime,
resourceValueConfigsMetadata
FROM google.securitycenter.simulations
WHERE organizationsId = '{{ organizationsId }}'
AND simulationsId = '{{ simulationsId }}'; 
```
