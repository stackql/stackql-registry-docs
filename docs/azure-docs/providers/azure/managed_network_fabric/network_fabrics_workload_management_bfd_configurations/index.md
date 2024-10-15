---
title: network_fabrics_workload_management_bfd_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabrics_workload_management_bfd_configurations
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_fabrics_workload_management_bfd_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_fabrics_workload_management_bfd_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_fabrics_workload_management_bfd_configurations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Updates the Workload Management BFD Configuration of the underlying resources in the given Network Fabric instance. |
