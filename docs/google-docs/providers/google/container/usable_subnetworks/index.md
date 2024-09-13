---
title: usable_subnetworks
hide_title: false
hide_table_of_contents: false
keywords:
  - usable_subnetworks
  - container
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

Creates, updates, deletes or gets an <code>usable_subnetwork</code> resource or lists <code>usable_subnetworks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usable_subnetworks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.container.usable_subnetworks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ipCidrRange" /> | `string` | The range of internal addresses that are owned by this subnetwork. |
| <CopyableCode code="network" /> | `string` | Network Name. Example: projects/my-project/global/networks/my-network |
| <CopyableCode code="secondaryIpRanges" /> | `array` | Secondary IP ranges. |
| <CopyableCode code="statusMessage" /> | `string` | A human readable status message representing the reasons for cases where the caller cannot use the secondary ranges under the subnet. For example if the secondary_ip_ranges is empty due to a permission issue, an insufficient permission message will be given by status_message. |
| <CopyableCode code="subnetwork" /> | `string` | Subnetwork Name. Example: projects/my-project/regions/us-central1/subnetworks/my-subnet |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_aggregated_usable_subnetworks_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists subnetworks that are usable for creating clusters in a project. |

## `SELECT` examples

Lists subnetworks that are usable for creating clusters in a project.

```sql
SELECT
ipCidrRange,
network,
secondaryIpRanges,
statusMessage,
subnetwork
FROM google.container.usable_subnetworks
WHERE projectsId = '{{ projectsId }}'; 
```
