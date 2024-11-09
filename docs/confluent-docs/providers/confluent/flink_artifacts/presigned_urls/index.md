---
title: presigned_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - presigned_urls
  - flink_artifacts
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>presigned_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>presigned_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.flink_artifacts.presigned_urls" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="presigned_upload_url_artifact_v1presigned_url" /> | `EXEC` | <CopyableCode code="" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Flink Artifact API EA](https://img.shields.io/badge/-Request%20Access%20To%20Flink%20Artifact%20API%20EA-%23bc8540)](mailto:ccloud-api-access+artifact-v1-early-access@confluent.io?subject=Request%20to%20join%20artifact/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20artifact/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Request a presigned upload URL to upload a Flink Artifact archive. |
