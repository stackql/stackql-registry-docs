---
title: scans
hide_title: false
hide_table_of_contents: false
keywords:
  - scans
  - ondemandscanning
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

Creates, updates, deletes or gets an <code>scan</code> resource or lists <code>scans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ondemandscanning.scans" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="analyze_packages" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Initiates an analysis of the provided packages. |
