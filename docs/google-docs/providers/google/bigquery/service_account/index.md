
---
title: service_account
hide_title: false
hide_table_of_contents: false
keywords:
  - service_account
  - bigquery
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

Creates, updates, deletes or gets an <code>service_account</code> resource or lists <code>service_account</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.service_account" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="email" /> | `string` | The service account email address. |
| <CopyableCode code="kind" /> | `string` | The resource type of the response. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_service_account" /> | `SELECT` | <CopyableCode code="projectId" /> | RPC to get the service account for a project used for interactions with Google Cloud KMS |

## `SELECT` examples

RPC to get the service account for a project used for interactions with Google Cloud KMS

```sql
SELECT
email,
kind
FROM google.bigquery.service_account
WHERE projectId = '{{ projectId }}'; 
```
