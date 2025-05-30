---
title: linkers_dapr_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - linkers_dapr_configurations
  - service_connector
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

Creates, updates, deletes, gets or lists a <code>linkers_dapr_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>linkers_dapr_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_connector.linkers_dapr_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List the dapr configuration supported by Service Connector. |

## `SELECT` examples

List the dapr configuration supported by Service Connector.


```sql
SELECT
properties
FROM azure.service_connector.linkers_dapr_configurations
WHERE resourceUri = '{{ resourceUri }}';
```