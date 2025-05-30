---
title: service_account
hide_title: false
hide_table_of_contents: false
keywords:
  - service_account
  - storage
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

Creates, updates, deletes, gets or lists a <code>service_account</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.service_account" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="email_address" /> | `string` | The ID of the notification. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For notifications, this is always storage#notification. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectId" /> | Get the email address of this project's Google Cloud Storage service account. |

## `SELECT` examples

Get the email address of this project's Google Cloud Storage service account.

```sql
SELECT
email_address,
kind
FROM google.storage.service_account
WHERE projectId = '{{ projectId }}';
```
