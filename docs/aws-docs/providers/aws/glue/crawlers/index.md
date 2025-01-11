---
title: crawlers
hide_title: false
hide_table_of_contents: false
keywords:
  - crawlers
  - glue
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

Creates, updates, deletes or gets a <code>crawler</code> resource or lists <code>crawlers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crawlers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Glue::Crawler</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.crawlers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="classifiers" /></td><td><code>array</code></td><td>A list of UTF-8 strings that specify the names of custom classifiers that are associated with the crawler.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the crawler.</td></tr>
<tr><td><CopyableCode code="schema_change_policy" /></td><td><code>object</code></td><td>The policy that specifies update and delete behaviors for the crawler. The policy tells the crawler what to do in the event that it detects a change in a table that already exists in the customer's database at the time of the crawl. The SchemaChangePolicy does not affect whether or how new tables and partitions are added. New tables and partitions are always created regardless of the SchemaChangePolicy on a crawler. The SchemaChangePolicy consists of two components, UpdateBehavior and DeleteBehavior.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>string</code></td><td>Crawler configuration information. This versioned JSON string allows users to specify aspects of a crawler's behavior.</td></tr>
<tr><td><CopyableCode code="recrawl_policy" /></td><td><code>object</code></td><td>When crawling an Amazon S3 data source after the first crawl is complete, specifies whether to crawl the entire dataset again or to crawl only folders that were added since the last crawler run. For more information, see Incremental Crawls in AWS Glue in the developer guide.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name of the database in which the crawler's output is stored.</td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>object</code></td><td>Specifies data stores to crawl.</td></tr>
<tr><td><CopyableCode code="crawler_security_configuration" /></td><td><code>string</code></td><td>The name of the SecurityConfiguration structure to be used by this crawler.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the crawler.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that's used to access customer resources, such as Amazon Simple Storage Service (Amazon S3) data.</td></tr>
<tr><td><CopyableCode code="lake_formation_configuration" /></td><td><code>object</code></td><td>Specifies AWS Lake Formation configuration settings for the crawler</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>A scheduling object using a cron statement to schedule an event.</td></tr>
<tr><td><CopyableCode code="table_prefix" /></td><td><code>string</code></td><td>The prefix added to the names of tables that are created.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags to use with this crawler.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html"><code>AWS::Glue::Crawler</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Role, Targets, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>crawlers</code> in a region.
```sql
SELECT
region,
classifiers,
description,
schema_change_policy,
configuration,
recrawl_policy,
database_name,
targets,
crawler_security_configuration,
name,
role,
lake_formation_configuration,
schedule,
table_prefix,
tags
FROM aws.glue.crawlers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>crawler</code>.
```sql
SELECT
region,
classifiers,
description,
schema_change_policy,
configuration,
recrawl_policy,
database_name,
targets,
crawler_security_configuration,
name,
role,
lake_formation_configuration,
schedule,
table_prefix,
tags
FROM aws.glue.crawlers
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>crawler</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.glue.crawlers (
 Targets,
 Role,
 region
)
SELECT 
'{{ Targets }}',
 '{{ Role }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.glue.crawlers (
 Classifiers,
 Description,
 SchemaChangePolicy,
 Configuration,
 RecrawlPolicy,
 DatabaseName,
 Targets,
 CrawlerSecurityConfiguration,
 Name,
 Role,
 LakeFormationConfiguration,
 Schedule,
 TablePrefix,
 Tags,
 region
)
SELECT 
 '{{ Classifiers }}',
 '{{ Description }}',
 '{{ SchemaChangePolicy }}',
 '{{ Configuration }}',
 '{{ RecrawlPolicy }}',
 '{{ DatabaseName }}',
 '{{ Targets }}',
 '{{ CrawlerSecurityConfiguration }}',
 '{{ Name }}',
 '{{ Role }}',
 '{{ LakeFormationConfiguration }}',
 '{{ Schedule }}',
 '{{ TablePrefix }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: crawler
    props:
      - name: Classifiers
        value:
          - '{{ Classifiers[0] }}'
      - name: Description
        value: '{{ Description }}'
      - name: SchemaChangePolicy
        value:
          UpdateBehavior: '{{ UpdateBehavior }}'
          DeleteBehavior: '{{ DeleteBehavior }}'
      - name: Configuration
        value: '{{ Configuration }}'
      - name: RecrawlPolicy
        value:
          RecrawlBehavior: '{{ RecrawlBehavior }}'
      - name: DatabaseName
        value: '{{ DatabaseName }}'
      - name: Targets
        value:
          S3Targets:
            - ConnectionName: '{{ ConnectionName }}'
              Path: '{{ Path }}'
              SampleSize: '{{ SampleSize }}'
              Exclusions:
                - '{{ Exclusions[0] }}'
              DlqEventQueueArn: '{{ DlqEventQueueArn }}'
              EventQueueArn: '{{ EventQueueArn }}'
          CatalogTargets:
            - ConnectionName: '{{ ConnectionName }}'
              DatabaseName: '{{ DatabaseName }}'
              DlqEventQueueArn: '{{ DlqEventQueueArn }}'
              Tables:
                - '{{ Tables[0] }}'
              EventQueueArn: '{{ EventQueueArn }}'
          DeltaTargets:
            - ConnectionName: '{{ ConnectionName }}'
              CreateNativeDeltaTable: '{{ CreateNativeDeltaTable }}'
              WriteManifest: '{{ WriteManifest }}'
              DeltaTables:
                - '{{ DeltaTables[0] }}'
          MongoDBTargets:
            - ConnectionName: '{{ ConnectionName }}'
              Path: '{{ Path }}'
          JdbcTargets:
            - ConnectionName: '{{ ConnectionName }}'
              Path: '{{ Path }}'
              Exclusions:
                - '{{ Exclusions[0] }}'
              EnableAdditionalMetadata:
                - '{{ EnableAdditionalMetadata[0] }}'
          DynamoDBTargets:
            - Path: '{{ Path }}'
          IcebergTargets:
            - ConnectionName: '{{ ConnectionName }}'
              Paths:
                - '{{ Paths[0] }}'
              Exclusions:
                - '{{ Exclusions[0] }}'
              MaximumTraversalDepth: '{{ MaximumTraversalDepth }}'
      - name: CrawlerSecurityConfiguration
        value: '{{ CrawlerSecurityConfiguration }}'
      - name: Name
        value: '{{ Name }}'
      - name: Role
        value: '{{ Role }}'
      - name: LakeFormationConfiguration
        value:
          UseLakeFormationCredentials: '{{ UseLakeFormationCredentials }}'
          AccountId: '{{ AccountId }}'
      - name: Schedule
        value:
          ScheduleExpression: '{{ ScheduleExpression }}'
      - name: TablePrefix
        value: '{{ TablePrefix }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.glue.crawlers
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>crawlers</code> resource, the following permissions are required:

### Create
```json
glue:CreateCrawler,
glue:GetCrawler,
glue:TagResource,
iam:PassRole
```

### Read
```json
glue:GetCrawler,
glue:GetTags,
iam:PassRole
```

### Update
```json
glue:UpdateCrawler,
glue:UntagResource,
glue:TagResource,
iam:PassRole
```

### Delete
```json
glue:DeleteCrawler,
glue:GetCrawler,
glue:StopCrawler,
iam:PassRole
```

### List
```json
glue:ListCrawlers,
iam:PassRole
```
