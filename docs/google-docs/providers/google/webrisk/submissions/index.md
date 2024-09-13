
---
title: submissions
hide_title: false
hide_table_of_contents: false
keywords:
  - submissions
  - webrisk
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

Creates, updates, deletes or gets an <code>submission</code> resource or lists <code>submissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>submissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.webrisk.submissions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a Submission of a URI suspected of containing phishing content to be reviewed. If the result verifies the existence of malicious phishing content, the site will be added to the [Google's Social Engineering lists](https://support.google.com/webmasters/answer/6350487/) in order to protect users that could get exposed to this threat in the future. Only allowlisted projects can use this method during Early Access. Please reach out to Sales or your customer engineer to obtain access. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>submissions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.webrisk.submissions (
projectsId,
uri
)
SELECT 
'{{ projectsId }}',
'{{ uri }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: uri
        value: '{{ uri }}'

```
</TabItem>
</Tabs>
