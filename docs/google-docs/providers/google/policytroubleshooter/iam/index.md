---
title: iam
hide_title: false
hide_table_of_contents: false
keywords:
  - iam
  - policytroubleshooter
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

Creates, updates, deletes or gets an <code>iam</code> resource or lists <code>iam</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iam</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.policytroubleshooter.iam" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="troubleshoot" /> | `EXEC` | <CopyableCode code="" /> | Checks whether a principal has a specific permission for a specific resource, and explains why the principal does or does not have that permission. |
