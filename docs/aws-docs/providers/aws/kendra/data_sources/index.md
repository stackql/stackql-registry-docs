---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - kendra
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


Used to retrieve a list of <code>data_sources</code> in a region or to create or delete a <code>data_sources</code> resource, use <code>data_source</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Kendra DataSource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendra.data_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="index_id" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
index_id
FROM aws.kendra.data_sources
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>data_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- data_source.iql (required properties only)
INSERT INTO aws.kendra.data_sources (
 Name,
 IndexId,
 Type,
 region
)
SELECT 
'{{ Name }}',
 '{{ IndexId }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- data_source.iql (all properties)
INSERT INTO aws.kendra.data_sources (
 Name,
 IndexId,
 Type,
 DataSourceConfiguration,
 Description,
 Schedule,
 RoleArn,
 Tags,
 CustomDocumentEnrichmentConfiguration,
 LanguageCode,
 region
)
SELECT 
 '{{ Name }}',
 '{{ IndexId }}',
 '{{ Type }}',
 '{{ DataSourceConfiguration }}',
 '{{ Description }}',
 '{{ Schedule }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ CustomDocumentEnrichmentConfiguration }}',
 '{{ LanguageCode }}',
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
  - name: data_source
    props:
      - name: Name
        value: '{{ Name }}'
      - name: IndexId
        value: '{{ IndexId }}'
      - name: Type
        value: '{{ Type }}'
      - name: DataSourceConfiguration
        value:
          S3Configuration:
            BucketName: '{{ BucketName }}'
            InclusionPrefixes:
              - '{{ InclusionPrefixes[0] }}'
            InclusionPatterns: null
            ExclusionPatterns: null
            DocumentsMetadataConfiguration:
              S3Prefix: '{{ S3Prefix }}'
            AccessControlListConfiguration:
              KeyPath: null
          SharePointConfiguration:
            SharePointVersion: '{{ SharePointVersion }}'
            Urls:
              - '{{ Urls[0] }}'
            SecretArn: '{{ SecretArn }}'
            CrawlAttachments: '{{ CrawlAttachments }}'
            UseChangeLog: '{{ UseChangeLog }}'
            InclusionPatterns: null
            ExclusionPatterns: null
            VpcConfiguration:
              SubnetIds:
                - '{{ SubnetIds[0] }}'
              SecurityGroupIds:
                - '{{ SecurityGroupIds[0] }}'
            FieldMappings:
              - DataSourceFieldName: '{{ DataSourceFieldName }}'
                DateFieldFormat: '{{ DateFieldFormat }}'
                IndexFieldName: '{{ IndexFieldName }}'
            DocumentTitleFieldName: null
            DisableLocalGroups: '{{ DisableLocalGroups }}'
            SslCertificateS3Path:
              Bucket: null
              Key: null
          SalesforceConfiguration:
            ServerUrl: null
            SecretArn: null
            StandardObjectConfigurations:
              - Name: '{{ Name }}'
                DocumentDataFieldName: null
                DocumentTitleFieldName: null
                FieldMappings: null
            KnowledgeArticleConfiguration:
              IncludedStates:
                - '{{ IncludedStates[0] }}'
              StandardKnowledgeArticleTypeConfiguration:
                DocumentDataFieldName: null
                DocumentTitleFieldName: null
                FieldMappings: null
              CustomKnowledgeArticleTypeConfigurations:
                - Name: '{{ Name }}'
                  DocumentDataFieldName: null
                  DocumentTitleFieldName: null
                  FieldMappings: null
            ChatterFeedConfiguration:
              DocumentDataFieldName: null
              DocumentTitleFieldName: null
              FieldMappings: null
              IncludeFilterTypes:
                - '{{ IncludeFilterTypes[0] }}'
            CrawlAttachments: '{{ CrawlAttachments }}'
            StandardObjectAttachmentConfiguration:
              DocumentTitleFieldName: null
              FieldMappings: null
            IncludeAttachmentFilePatterns: null
            ExcludeAttachmentFilePatterns: null
          OneDriveConfiguration:
            TenantDomain: '{{ TenantDomain }}'
            SecretArn: null
            OneDriveUsers:
              OneDriveUserList:
                - '{{ OneDriveUserList[0] }}'
              OneDriveUserS3Path: null
            InclusionPatterns: null
            ExclusionPatterns: null
            FieldMappings: null
            DisableLocalGroups: null
          ServiceNowConfiguration:
            HostUrl: '{{ HostUrl }}'
            SecretArn: null
            ServiceNowBuildVersion: '{{ ServiceNowBuildVersion }}'
            AuthenticationType: '{{ AuthenticationType }}'
            KnowledgeArticleConfiguration:
              CrawlAttachments: '{{ CrawlAttachments }}'
              IncludeAttachmentFilePatterns: null
              ExcludeAttachmentFilePatterns: null
              DocumentDataFieldName: null
              DocumentTitleFieldName: null
              FieldMappings: null
              FilterQuery: '{{ FilterQuery }}'
            ServiceCatalogConfiguration:
              CrawlAttachments: '{{ CrawlAttachments }}'
              IncludeAttachmentFilePatterns: null
              ExcludeAttachmentFilePatterns: null
              DocumentDataFieldName: null
              DocumentTitleFieldName: null
              FieldMappings: null
          DatabaseConfiguration:
            DatabaseEngineType: '{{ DatabaseEngineType }}'
            ConnectionConfiguration:
              DatabaseHost: '{{ DatabaseHost }}'
              DatabasePort: '{{ DatabasePort }}'
              DatabaseName: '{{ DatabaseName }}'
              TableName: '{{ TableName }}'
              SecretArn: null
            VpcConfiguration: null
            ColumnConfiguration:
              DocumentIdColumnName: '{{ DocumentIdColumnName }}'
              DocumentDataColumnName: null
              DocumentTitleColumnName: null
              FieldMappings: null
              ChangeDetectingColumns:
                - null
            AclConfiguration:
              AllowedGroupsColumnName: null
            SqlConfiguration:
              QueryIdentifiersEnclosingOption: '{{ QueryIdentifiersEnclosingOption }}'
          ConfluenceConfiguration:
            ServerUrl: null
            SecretArn: null
            Version: '{{ Version }}'
            SpaceConfiguration:
              CrawlPersonalSpaces: '{{ CrawlPersonalSpaces }}'
              CrawlArchivedSpaces: '{{ CrawlArchivedSpaces }}'
              IncludeSpaces:
                - '{{ IncludeSpaces[0] }}'
              ExcludeSpaces: null
              SpaceFieldMappings:
                - DataSourceFieldName: '{{ DataSourceFieldName }}'
                  DateFieldFormat: null
                  IndexFieldName: null
            PageConfiguration:
              PageFieldMappings:
                - DataSourceFieldName: '{{ DataSourceFieldName }}'
                  DateFieldFormat: null
                  IndexFieldName: null
            BlogConfiguration:
              BlogFieldMappings:
                - DataSourceFieldName: '{{ DataSourceFieldName }}'
                  DateFieldFormat: null
                  IndexFieldName: null
            AttachmentConfiguration:
              CrawlAttachments: '{{ CrawlAttachments }}'
              AttachmentFieldMappings:
                - DataSourceFieldName: '{{ DataSourceFieldName }}'
                  DateFieldFormat: null
                  IndexFieldName: null
            VpcConfiguration: null
            InclusionPatterns: null
            ExclusionPatterns: null
          GoogleDriveConfiguration:
            SecretArn: null
            InclusionPatterns: null
            ExclusionPatterns: null
            FieldMappings: null
            ExcludeMimeTypes:
              - '{{ ExcludeMimeTypes[0] }}'
            ExcludeUserAccounts:
              - '{{ ExcludeUserAccounts[0] }}'
            ExcludeSharedDrives:
              - '{{ ExcludeSharedDrives[0] }}'
          WebCrawlerConfiguration:
            Urls:
              SeedUrlConfiguration:
                SeedUrls:
                  - '{{ SeedUrls[0] }}'
                WebCrawlerMode: '{{ WebCrawlerMode }}'
              SiteMapsConfiguration:
                SiteMaps:
                  - '{{ SiteMaps[0] }}'
            CrawlDepth: '{{ CrawlDepth }}'
            MaxLinksPerPage: '{{ MaxLinksPerPage }}'
            MaxContentSizePerPageInMegaBytes: null
            MaxUrlsPerMinuteCrawlRate: '{{ MaxUrlsPerMinuteCrawlRate }}'
            UrlInclusionPatterns: null
            UrlExclusionPatterns: null
            ProxyConfiguration:
              Host: '{{ Host }}'
              Port: '{{ Port }}'
              Credentials: null
            AuthenticationConfiguration:
              BasicAuthentication:
                - Host: '{{ Host }}'
                  Port: '{{ Port }}'
                  Credentials: null
          WorkDocsConfiguration:
            OrganizationId: '{{ OrganizationId }}'
            CrawlComments: '{{ CrawlComments }}'
            UseChangeLog: '{{ UseChangeLog }}'
            InclusionPatterns: null
            ExclusionPatterns: null
            FieldMappings: null
      - name: Description
        value: '{{ Description }}'
      - name: Schedule
        value: '{{ Schedule }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CustomDocumentEnrichmentConfiguration
        value:
          InlineConfigurations:
            - Condition:
                ConditionDocumentAttributeKey: '{{ ConditionDocumentAttributeKey }}'
                Operator: '{{ Operator }}'
                ConditionOnValue:
                  StringValue: '{{ StringValue }}'
                  StringListValue:
                    - '{{ StringListValue[0] }}'
                  LongValue: '{{ LongValue }}'
                  DateValue: '{{ DateValue }}'
              Target:
                TargetDocumentAttributeKey: null
                TargetDocumentAttributeValueDeletion: '{{ TargetDocumentAttributeValueDeletion }}'
                TargetDocumentAttributeValue: null
              DocumentContentDeletion: '{{ DocumentContentDeletion }}'
          PreExtractionHookConfiguration:
            InvocationCondition: null
            LambdaArn: '{{ LambdaArn }}'
            S3Bucket: null
          PostExtractionHookConfiguration: null
          RoleArn: null
      - name: LanguageCode
        value: '{{ LanguageCode }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.kendra.data_sources
WHERE data__Identifier = '<Id|IndexId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Create
```json
kendra:CreateDataSource,
kendra:DescribeDataSource,
kendra:ListTagsForResource,
iam:PassRole,
kendra:TagResource
```

### Delete
```json
kendra:DescribeDataSource,
kendra:DeleteDataSource
```

### List
```json
kendra:ListDataSources
```

