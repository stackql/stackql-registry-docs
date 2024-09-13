---
title: consents_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - consents_revision
  - healthcare
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

Creates, updates, deletes or gets an <code>consents_revision</code> resource or lists <code>consents_revision</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consents_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.consents_revision" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_revision" /> | `DELETE` | <CopyableCode code="consentStoresId, consentsId, datasetsId, locationsId, projectsId" /> | Deletes the specified revision of a Consent. An INVALID_ARGUMENT error occurs if the specified revision is the latest revision. |

## `DELETE` example

Deletes the specified consents_revision resource.

```sql
DELETE FROM google.healthcare.consents_revision
WHERE consentStoresId = '{{ consentStoresId }}'
AND consentsId = '{{ consentsId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
