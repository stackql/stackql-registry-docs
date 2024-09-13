---
title: clientmetadata
hide_title: false
hide_table_of_contents: false
keywords:
  - clientmetadata
  - integrations
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

Creates, updates, deletes or gets an <code>clientmetadatum</code> resource or lists <code>clientmetadata</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clientmetadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.clientmetadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Metadata information for the given project |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_get_clientmetadata" /> | `SELECT` | <CopyableCode code="projectsId" /> | Gets the metadata info for the requested client |

## `SELECT` examples

Gets the metadata info for the requested client

```sql
SELECT
properties
FROM google.integrations.clientmetadata
WHERE projectsId = '{{ projectsId }}'; 
```
