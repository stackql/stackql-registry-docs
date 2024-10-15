---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - container_instances
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

Creates, updates, deletes, gets or lists a <code>containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instances.containers" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="attach" /> | `EXEC` | <CopyableCode code="containerGroupName, containerName, resourceGroupName, subscriptionId" /> | Attach to the output stream of a specific container instance in a specified resource group and container group. |
| <CopyableCode code="execute_command" /> | `EXEC` | <CopyableCode code="containerGroupName, containerName, resourceGroupName, subscriptionId" /> | Executes a command for a specific container instance in a specified resource group and container group. |
