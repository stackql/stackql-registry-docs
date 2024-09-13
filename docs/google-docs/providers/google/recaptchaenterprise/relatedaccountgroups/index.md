
---
title: relatedaccountgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - relatedaccountgroups
  - recaptchaenterprise
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

Creates, updates, deletes or gets an <code>relatedaccountgroup</code> resource or lists <code>relatedaccountgroups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relatedaccountgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.relatedaccountgroups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Identifier. The resource name for the related account group in the format `projects/{project}/relatedaccountgroups/{related_account_group}`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | List groups of related accounts. |

## `SELECT` examples

List groups of related accounts.

```sql
SELECT
name
FROM google.recaptchaenterprise.relatedaccountgroups
WHERE projectsId = '{{ projectsId }}'; 
```
