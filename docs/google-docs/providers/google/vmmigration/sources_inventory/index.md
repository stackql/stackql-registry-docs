---
title: sources_inventory
hide_title: false
hide_table_of_contents: false
keywords:
  - sources_inventory
  - vmmigration
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

Creates, updates, deletes, gets or lists a <code>sources_inventory</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sources_inventory</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.sources_inventory" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="awsVms" /> | `object` | AWSVmsDetails describes VMs in AWS. |
| <CopyableCode code="azureVms" /> | `object` | AzureVmsDetails describes VMs in Azure. |
| <CopyableCode code="nextPageToken" /> | `string` | Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the source was last queried (if the result is from the cache). |
| <CopyableCode code="vmwareVms" /> | `object` | VmwareVmsDetails describes VMs in vCenter. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_inventory" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | List remote source's inventory of VMs. The remote source is the onprem vCenter (remote in the sense it's not in Compute Engine). The inventory describes the list of existing VMs in that source. Note that this operation lists the VMs on the remote source, as opposed to listing the MigratingVms resources in the vmmigration service. |

## `SELECT` examples

List remote source's inventory of VMs. The remote source is the onprem vCenter (remote in the sense it's not in Compute Engine). The inventory describes the list of existing VMs in that source. Note that this operation lists the VMs on the remote source, as opposed to listing the MigratingVms resources in the vmmigration service.

```sql
SELECT
awsVms,
azureVms,
nextPageToken,
updateTime,
vmwareVms
FROM google.vmmigration.sources_inventory
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}'; 
```
