---
title: organizations_api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations_api_keys
  - elastic
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

Creates, updates, deletes, gets or lists a <code>organizations_api_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations_api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.organizations_api_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Fetch User API Key from internal database, if it was generated and stored while creating the Elasticsearch Organization. |

## `SELECT` examples

Fetch User API Key from internal database, if it was generated and stored while creating the Elasticsearch Organization.


```sql
SELECT
properties
FROM azure_isv.elastic.organizations_api_keys
WHERE subscriptionId = '{{ subscriptionId }}';
```