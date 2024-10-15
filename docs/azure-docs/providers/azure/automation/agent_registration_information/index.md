---
title: agent_registration_information
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_registration_information
  - automation
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

Creates, updates, deletes, gets or lists a <code>agent_registration_information</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_registration_information</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.agent_registration_information" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the id. |
| <CopyableCode code="dscMetaConfiguration" /> | `string` | Gets or sets the dsc meta configuration. |
| <CopyableCode code="endpoint" /> | `string` | Gets or sets the dsc server endpoint. |
| <CopyableCode code="keys" /> | `object` | Definition of the agent registration keys. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve the automation agent registration information. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId, data__keyName" /> | Regenerate a primary or secondary agent registration key |

## `SELECT` examples

Retrieve the automation agent registration information.


```sql
SELECT
id,
dscMetaConfiguration,
endpoint,
keys
FROM azure.automation.agent_registration_information
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```