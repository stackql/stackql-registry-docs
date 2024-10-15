---
title: tenant_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_configurations
  - api_management
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

Creates, updates, deletes, gets or lists a <code>tenant_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_configurations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="deploy" /> | `EXEC` | <CopyableCode code="configurationName, resourceGroupName, serviceName, subscriptionId" /> | This operation applies changes from the specified Git branch to the configuration database. This is a long running operation and could take several minutes to complete. |
| <CopyableCode code="save" /> | `EXEC` | <CopyableCode code="configurationName, resourceGroupName, serviceName, subscriptionId" /> | This operation creates a commit with the current configuration snapshot to the specified branch in the repository. This is a long running operation and could take several minutes to complete. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="configurationName, resourceGroupName, serviceName, subscriptionId" /> | This operation validates the changes in the specified Git branch. This is a long running operation and could take several minutes to complete. |
