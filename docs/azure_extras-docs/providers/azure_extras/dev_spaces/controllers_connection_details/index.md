---
title: controllers_connection_details
hide_title: false
hide_table_of_contents: false
keywords:
  - controllers_connection_details
  - dev_spaces
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

Creates, updates, deletes, gets or lists a <code>controllers_connection_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>controllers_connection_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.dev_spaces.controllers_connection_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectionDetailsList" /> | `array` | List of Azure Dev Spaces Controller connection details. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__targetContainerHostResourceId" /> | Lists connection details for the underlying container resources of an Azure Dev Spaces Controller. |

## `SELECT` examples

Lists connection details for the underlying container resources of an Azure Dev Spaces Controller.


```sql
SELECT
connectionDetailsList
FROM azure_extras.dev_spaces.controllers_connection_details
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__targetContainerHostResourceId = '{{ data__targetContainerHostResourceId }}';
```