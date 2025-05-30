---
title: basic_publishing_credentials_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - basic_publishing_credentials_policies
  - app_service
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

Creates, updates, deletes, gets or lists a <code>basic_publishing_credentials_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>basic_publishing_credentials_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.basic_publishing_credentials_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | CsmPublishingCredentialsPoliciesEntity resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site. |

## `SELECT` examples

Description for Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.basic_publishing_credentials_policies
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```