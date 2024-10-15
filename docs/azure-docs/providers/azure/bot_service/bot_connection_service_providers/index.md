---
title: bot_connection_service_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_connection_service_providers
  - bot_service
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

Creates, updates, deletes, gets or lists a <code>bot_connection_service_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_connection_service_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.bot_connection_service_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Object used to describe a Service Provider supported by Bot Service |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the available Service Providers for creating Connection Settings |

## `SELECT` examples

Lists the available Service Providers for creating Connection Settings


```sql
SELECT
properties
FROM azure.bot_service.bot_connection_service_providers
WHERE subscriptionId = '{{ subscriptionId }}';
```