---
title: builds_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - builds_list_only
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>builds</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/builds/"><code>builds</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builds_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GameLift::Build</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.builds_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="build_id" /></td><td><code>string</code></td><td>A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label that is associated with a build. Build names do not need to be unique.</td></tr>
<tr><td><CopyableCode code="operating_system" /></td><td><code>string</code></td><td>The operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.</td></tr>
<tr><td><CopyableCode code="storage_location" /></td><td><code>object</code></td><td>Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Version information that is associated with this build. Version strings do not need to be unique.</td></tr>
<tr><td><CopyableCode code="server_sdk_version" /></td><td><code>string</code></td><td>A server SDK version you used when integrating your game server build with Amazon GameLift. By default Amazon GameLift sets this value to 4.0.2.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>builds</code> in a region.
```sql
SELECT
region,
build_id
FROM aws.gamelift.builds_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>builds_list_only</code> resource, see <a href="/providers/aws/gamelift/builds/#permissions"><code>builds</code></a>


